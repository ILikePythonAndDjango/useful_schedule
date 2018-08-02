
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
			console.log(this.sequence)
			if (sequence.length === 0) alert("Sequence is empty")
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

Vue.component('modal', {
  template: '#modal-template',
})

var modal_window = new Vue({
	el: '#modal_window',
	data: {

		//management for modal windows
		showModal: false,
		showCreateGoalModal: false,
		showCreateNoteModal: false,
		showCreatScheduleModal: false,
		showCreateTask: false,

		//fields for creating new goal
		newGoalTitle: '',
		newGoalContent: '',
		newGoalDeadline: null,

		//fields for creating new note
		newNoteTime: null,
		newNoteDate: null,
		newNoteText: '',

		//fields for creating new schedule
	},
	methods: {
		createGoal: function () {
			var FD = new FormData()
			FD.append("title", this.newGoalTitle)
			FD.append("content", this.newGoalContent)
			FD.append("deadline", this.newGoalDeadline)

			axios.post("/goals/1/", FD)
			.then(function (response) {
				if (response.data.status === 'ok') {
					console.log(response.data)
					alert("Goal was created")
				} else {
					alert(response.data.message)
				}
			}).catch(function (error) {
				alert(error)
			})
		},
		createNote: function () {
			var FD = new FormData();
			FD.append("time", this.newNoteTime)
			FD.append("date", this.newNoteDate)
			FD.append("text", this.newNoteText)

			axios.post("/notes/1/", FD)
			.then(function (response) {
				if (response.data.status === 'ok') {
					console.log(data)
					alert("Note was created")
					console.log(response.data.new_note)
				} else {
					alert(response.data.message)
				}
			}).catch(function (error) {
				alert(error)
			})
		},
	},
})