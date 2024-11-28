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

        let success = false
        await useFetch(`${config.public.serverUrl}/o/token/`, {
            method: 'post',
            headers: { 'Content-Type': "application/x-www-form-urlencoded" },
            body: urlencoded
        }).then(response => {
            if (response.data.value == null) {
                success = false
            } else {
                tokens.value = response.data.value
                success = true
            }
        }).catch(error => {
            success = false
        })

        if (success) {
            await getUserInfo()
        }

        return success
    }

    async function getUserInfo() {
        return await useFetch(`${config.public.serverUrl}/users/profile/`, {
            headers: {
                "Authorization": `Bearer ${accessToken.value}`
            }
        }).then(response => {
            if (response.data.value == null) {
                return false
            } else {
                console.log('info', response.data.value)
                userInfo.value = response.data.value
                return true
            }
        }).catch(error => {
            return false
        })
    }

    return { userInfo, accessToken, authenticate, getUserInfo }
})