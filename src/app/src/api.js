import axios from "axios";

var dummyData = [
	{
		_id: "1",
		text: "Task 1",
	},
	{
		_id: "2",
		text: "assignment 2",
	},
	{
		_id: "3",
		text: "Dummy text 3",
	},
];

export const fetchToDoList = async () => {
	return dummyData;
};

var cnt = 3;
export const addToDoItem = async (todoItem) => {
	console.log("AddToDoItem" + todoItem);
	cnt++;
	const res = { _id: `${cnt}`, text: todoItem };
	dummyData = [...dummyData, res];
	return res;
};

export const updateToDoItem = async (todoId, updatedToDoItem) => {
	console.log("UpdateToDoItem" + updatedToDoItem);
	const res = { _id: todoId, text: updatedToDoItem };
	dummyData = dummyData.map((toDoItem) => {
		return toDoItem._Id === todoId ? res : toDoItem;
	});
	return res;
};

export const deleteToDo = async (todoId) => {
	console.log(todoId);
	dummyData = dummyData.filter((e) => {
		return e._Id !== todoId;
	});
	return;
};
