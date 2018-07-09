var DIV = '#content';
function getButton(content, funct_string='') {
	return `<button class="btn btn-outline-success my-2 my-sm-0" type="submit" onclick="${funct_string}">${content}</button>`;
}

function ajaxRequest(url, render=renderUlList, properties={}, dataType='json', cache=false) {
	$.ajax({
		type: 'GET',
		url: url,
		data: properties,
		dataType: dataType,
		cache: cache,
		success: render
	})
}

function getUlList (sequence) {
	var result = '';
	for (var el = 0; el < sequence.length; el++) {
		result += `<li onclick="ajaxRequest('${sequence[el].url}', renderObject)">${sequence[el].title}</li>`;
	}
	return `<ul>${result}</ul>`;
}

function renderUlList(data) {
	jQuery(DIV).html(getUlList(data.sequence) + getButton('Create'));
}

function getGoal(goal) {
	return `<h3>${goal.title}</h3><br><h5>${goal.deadline}</h5><br><p>${goal.content}</p>`;
}

function getCost(cost) {
	return `${cost.thing} -- ${cost.cost}`;
}

function getNote(note) {
	var result = `<h3>${note.date}</h3><hr><h5>${note.time}</h5><p>${note.text}</p><ul>`;
	note.cost_control.forEach((cost) => {result += `<li>${getCost(cost)}</li>`;});
	return result + '</ul>';
}

function getSchedule(schedule) {
	var result = `<h3>${schedule.title}</h3>`;
	schedule.tasks.forEach((task) => result += `<dic class='task'><hr><div class="task_content"><h5>${task.title}</h5><p>${task.begin} -- ${task.end}</p><p>${task.description}</p></div><div class="buttons"><div class="uniform">${getButton('Uniform')}</div><div class="remove">${getButton('Remove')}</div></div></div>`);
	return result;
}

function getObject(data) {
	if (data.status === 'error') {return data.msg;} 
	for (var property in data) {
		switch (property) {
			case 'goal': return getGoal(data.goal); break;
			case 'note': return getNote(data.note); break;
			case 'cost': return getCost(data.cost); break;
			case 'schedule': return getSchedule(data.schedule); break;
		}
	}
}

function renderObject(data) {
	jQuery(DIV).html(getObject(data));
}	