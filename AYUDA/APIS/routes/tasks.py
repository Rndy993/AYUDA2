from flask import Blueprint, request, jsonify
from models import db, Task
from schemas import TaskSchema
from utils.jwt_utils import token_required

tasks = Blueprint('tasks', __name__)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@tasks.route('/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    all_tasks = Task.query.all()
    return tasks_schema.jsonify(all_tasks), 200

@tasks.route('/tasks/<int:id>', methods=['GET'])
@token_required
def get_task(current_user, id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'message': 'Task not found!'}), 404
    return task_schema.jsonify(task), 200

@tasks.route('/tasks', methods=['POST'])
@token_required
def create_task(current_user):
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], status=data['status'], assigned_to=data['assigned_to'], created_at=data['created_at'])
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task), 201

@tasks.route('/tasks/<int:id>', methods=['PUT'])
@token_required
def update_task(current_user, id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'message': 'Task not found!'}), 404

    data = request.get_json()
    task.status = data['status']
    db.session.commit()
    return task_schema.jsonify(task), 200

@tasks.route('/tasks/<int:id>', methods=['DELETE'])
@token_required
def delete_task(current_user, id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'message': 'Task not found!'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted!'}), 200
