Vue.component('items',{
	props: ['item'],
	template: '<li><button v-on:click="renderObject(1)">{{ item.title }}</button></li>',
})

var app = new Vue({
	el: '#app',
	data: {
		sequence: [],
		obj: {
			title: '',
			content: '',
			deadline: '',
		},
	},
	methods: {
		renderSequence: function (url) {
			console.log(`get request on ${url}`)
			axios.get(url)
			.then(function (response) {
				if (response.data.status === 'error') {
					console.log('error')
					alert(response.data.message)
				} else {
					console.log("OK")
					this.sequence = response.data.sequence
				}
			}).catch(function (e) {
				alert(e)
				console.log("other errors")
			})
			console.log('end')
		},
		renderObject: function (id) {
			console.log("I'am stared!")
			for (goal of this.sequence) {
				console.log(goal.ic)
				if (id === goal.id) {
					console.log(goal)
					axiox.get(goal.url)
					.then(function (response) {
						this.obj = response.data.goal
						console.log(response.data.goal)
					}).catch(function (error) {
						alert(error)
					})
					this.sequence = []
					break
				}
			}
			console.log("I'am ended!")
		},
	},
})