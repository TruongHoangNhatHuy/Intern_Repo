import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
    const config = useRuntimeConfig()
    const tokens = ref(null)
    const userInfo = ref(null)
    const accessToken = computed(() => tokens.value?.access_token || null)

    // login
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
            const success = await getUserInfo()
            return success
        } else {
            console.warn(error.value)
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
            console.warn(error.value)
            return false
        }
    }

    // logout
    async function revokeAuth() {
        if (accessToken==null) return false

        const urlencoded = new URLSearchParams()
        urlencoded.append('token', accessToken)
        urlencoded.append('client_id', config.public.oauthId)
        urlencoded.append('client_secret', config.public.oauthSecret)

        const { data, status, error } = await useFetch(`${config.public.serverUrl}/o/revoke_token/`, {
            method: 'post',
            headers: { 'Content-Type': "application/x-www-form-urlencoded" },
            body: urlencoded
        })

        if (status.value==`success`) {
            tokens.value = null
            userInfo.value = null
            return true
        } else {
            console.warn(error.value)
            return false
        }
    }

    return { userInfo, tokens, accessToken, authenticate, getUserInfo, revokeAuth }
})