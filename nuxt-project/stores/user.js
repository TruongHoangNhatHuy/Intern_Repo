import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
    const config = useRuntimeConfig()
    const tokens = ref(null)
    const userInfo = ref(null)
    const accessToken = computed(() => tokens.value?.access_token || null)

    async function authenticate(username, password) {
        const urlencoded = new URLSearchParams()
        urlencoded.append('grant_type', 'password')
        urlencoded.append('username', username)
        urlencoded.append('password', password)
        urlencoded.append('client_id', config.public.oauthId)
        urlencoded.append('client_secret', config.public.oauthSecret)

        const { data, status, error } = await useFetch(`${config.public.serverUrl}/o/token/`, {
            method: 'post',
            headers: { 'Content-Type': "application/x-www-form-urlencoded" },
            body: urlencoded
        })

        if (status.value==`success` && data.value!=null) {
            tokens.value = data.value
            await getUserInfo()
            return true
        } else {
            console.log(error.value)
            return false
        }
    }

    async function getUserInfo() {
        const { data, status, error } = await useFetch(`${config.public.serverUrl}/users/profile/`, {
            headers: {
                "Authorization": `Bearer ${accessToken.value}`
            }
        })

        if (status.value==`success` && data.value!=null) {
            userInfo.value = data.value
            return true
        } else {
            console.log(error.value)
            return false
        }
    }

    return { userInfo, accessToken, authenticate, getUserInfo }
})