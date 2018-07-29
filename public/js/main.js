Vue.component('items',{
	props: ['item'],
	template: '<li>{{ item.title }}</li>',
})

var app = new Vue({
	el: '#app',
	data: {
		sequence: [],
	},
	methods: {
		renderSequence: function (url) {
			axios.get(url)
			.then(function (response) {
				if (response.data.status === 'error') {
					alert(response.data.message)
				} else {
					this.sequence = response.data.sequence
				}
			}).catch(function (e) {
				alert(e)
			})
		},
	},
})
	
var nav = new Vue({
	el: '#navigation',
	data: {
		logInButtonText: "Log in",
		logOutButtonText: "Log out",
		signUpButtonText: "Sign up",
	},
	methods: {
		logOut: function () {
			axios.post('/logout/', {})
			.then(function (response) {
				alert(response.data.message)
			}).catch(function (error) {
				alert(error)
			})
		},
	},
})

var login = new Vue({
	el: '#login',
	data: {
		username: '',
		password: '',
	},
	methods: {
		logIn: function () {
			if (this.username === '' || this.password === '') {
				alert("Yod haven't put username or password")
			} else {
				var FD = new FormData()
				FD.append("username", this.username)
				FD.append("password", this.password)
				axios.post("/login/", FD)
				.then(function (response) {
					alert(response.data.message)
					window.history.go(-1)
				}).catch(function (error) {
					alert(error)
				})
				this.username = ''
				this.password = ''
			}
		}
	},
})

var register = new Vue({
	el: '#register',
	data: {
		email: '',
		username: '',
		password: '',
	},
	methods: {
		signUp: function () {
			if (this.username === '' || this.password === '' || this.email === '') {
				alert("Yod haven't put username or password or e-mail")
			} else {
				var FD = new FormData()
				FD.append('username', this.username)
				FD.append("password", this.password)
				FD.append('email', this.email)
				axios.post("/signup/", FD)
				.then(function (response) {
					alert(response.data.message)
					window.history.go(-1)
					
				}).catch(function (error) {
					alert(error)
				})
				this.username = ''
				this.password = ''
				this.email = ''
			}
		},
	},
})