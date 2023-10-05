import axios from 'axios';
const BASE_URL = "http://localhost:8000/"
const todosUrl = `${BASE_URL}/todos/`

export const fetchToDoList = async () => {
    try {
        const res = await axios.get(todosUrl);
        return res.data;
    } catch (e) {
        console.error('Error occured while fetching todo list:', e);
        throw e;
    }
};

export const addToDoItem = async (todoItem) => {
    try {
		JSON.stringify(todoItem);
        const res = await axios.post(todosUrl, { text: todoItem });
        return res.data;
    } catch (e) {
        console.error('Error occured while adding new todo:', e);
        throw e;
    }
};
export const updateToDoItem = async (todoId, updatedToDoItem) => {
    try {
        const res = await axios.put(todosUrl, {
            _id: todoId,
			text: updatedToDoItem,
        });
        return res.data;
    } catch (e) {
        console.error('Error occured while updating todo:', e);
        throw e;
    }
};

export const deleteToDo = async (todoId) => {
    try {
        const res = await axios.delete(todosUrl,{
            data: {
                _id: todoId
            }
        });
        return res.data;
    } catch (e) {
        console.e('Error occured while deleting todo:', e);
        throw e;
    }
};
