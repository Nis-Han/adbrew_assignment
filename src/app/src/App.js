import "./App.css";
import React, { useState, useEffect } from "react";
import { fetchToDoList, addToDoItem, updateToDoItem, deleteToDo } from "./api";

export function App() {
	const [toDoList, setToDoList] = useState([]);
	const [newToDoItem, setNewToDoItem] = useState("");
	const [updatedToDoItem, setUpdatedToDoItem] = useState({
		id: null,
		text: "",
	});

	useEffect(() => {
		fetchToDoList()
			.then((data) => setToDoList(data))
			.catch((err) =>
				console.error("Error occured while fetching toDo list:", err)
			);
	}, []);

	const handleAddToDoItem = (e) => {
		e.preventDefault();
		addToDoItem(newToDoItem)
			.then((data) => {
				setToDoList([...toDoList, data]);
				setNewToDoItem("");
			})
			.catch((err) => console.error("Error occured while adding a toDo:", err));
	};

	const handleupdateToDoItem = (toDoId, updatedToDoItem) => {
		updateToDoItem(toDoId, updatedToDoItem)
			.then((data) => {
				setToDoList(() => {
					const lol = toDoList.map((toDo) =>
						toDo._id === toDoId ? data : toDo
					);
					return lol;
				});
				setUpdatedToDoItem({ id: null, text: "" });
			})
			.catch((err) => console.error("Error updating toDo:", err));
	};

	const handleDeleteToDo = (toDoId) => {
		deleteToDo(toDoId)
			.then(() => {
				setToDoList(toDoList.filter((toDo) => toDo._id !== toDoId));
			})
			.catch((err) => console.error("Error occured while deleting toDo:", err));
	};

	return (
		<div className="App">
			<div>
				<h1>List of ToDos</h1>
				<ul>
					{toDoList.map((toDo) => (
						<li key={toDo._id}>
							{toDo._id === updatedToDoItem.id ? (
								<div>
									<input
										type="text"
										value={updatedToDoItem.text}
										onChange={(e) =>
											setUpdatedToDoItem({
												id: updatedToDoItem.id,
												text: e.target.value,
											})
										}
									/>
									<button
										onClick={() =>
											handleupdateToDoItem(toDo._id, updatedToDoItem.text)
										}
									>
										Save
									</button>
								</div>
							) : (
								<div>
									{toDo.text}
									<button
										onClick={() =>
											setUpdatedToDoItem({ id: toDo._id, text: toDo.text })
										}
									>
										Edit
									</button>
									<button onClick={() => handleDeleteToDo(toDo._id)}>
										Delete
									</button>
								</div>
							)}
						</li>
					))}
				</ul>
			</div>
			<div>
				<h1>Create a ToDo</h1>
				<form onSubmit={handleAddToDoItem}>
					<div>
						<label htmlFor="toDo">ToDo: </label>
						<input
							type="text"
							value={newToDoItem}
							onChange={(e) => setNewToDoItem(e.target.value)}
						/>
					</div>
					<div style={{ marginTop: "5px" }}>
						<button type="submit">Add ToDo!</button>
					</div>
				</form>
			</div>
		</div>
	);
}

export default App;
