
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
			if (this.sequence.length === 0) alert("Sequence is empty")
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


//Vue component for working with modal windows
Vue.component('modal', {
  template: '#modal-template',
})

var modal_window = new Vue({
	el: '#modal_window',
	data: {

		//management for modal windows
		showModal: false,
		showCreatingGoalModal: false,
		showCreatingNoteModal: false,
		showCreatingScheduleModal: false,
		showCreatingTask: false,
		showCreateingCostControl: false,

		//fields for creating new goal
		newGoalTitle: '',
		newGoalContent: '',
		newGoalDeadline: null,

		//fields for creating new note
		newNoteTime: null,
		newNoteDate: null,
		newNoteText: '',
		newNoteCostControls: [],

		//fields for creating new cost control
		newCostControlThing: '',
		newCostControlCost: 0,

		//fields for creating new schedule
	},
	methods: {
		//Methods that listed below it's methods for working with goals
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

		//Methods that listed below it's methods for working with notes
		createNote: function () {
			var FD = new FormData();
			FD.append("text", this.newNoteText)
			FD.append("cost_controls_id", this.newNoteCostControls.map((costControl) => {costControl.id.get}))

			console.log(this.newNoteCostControls.map((costControl) => {costControl.id}))
			console.log(this.newNoteCostControls)

			axios.post("/notes/1/", FD)
			.then(function (response) {
				if (response.data.status === 'ok') {
					console.log(response.data)
					alert("Note was created")
					console.log(response.data.new_note)
				} else {
					alert(response.data.message)
				}
			}).catch(function (error) {
				alert(error)
			})
		},
		appendNewCostControlToNote: function () {
			this.showCreateingCostControl = true
		},

		//Methods that listed below it's methods for working with cost controls
		createNewCostControl: function () {
			var link_on_this = this

			var FD = new FormData();
			FD.append("thing", this.newCostControlThing)
			FD.append("cost", this.newCostControlCost)

			axios.post("/things/1/", FD)
			.then(function (response) {
				console.log(response.data)
				alert("Cost control was created!!")
				link_on_this.newNoteCostControls.push({
					id: response.data.new_cost_control.id,
					thing: response.data.new_cost_control.thing,
				})
			}).catch(function (error) {
				alert(error)
			})
		},
		getNewCostControl: function () {
			var link_on_this = this;
			axios.get("/things/1/?new=1")
			.then(function (response) {
				link_on_this.newNoteCostControls.push(response.data.latest_cost_control)
			}).catch(function (error) {
				alert(error)
			})
		},
	},
})