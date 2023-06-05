from flask import Flask, jsonify, request

app = Flask(__name__)

# 假设这是一个用户数据库
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]


# 获取所有用户信息
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# 获取指定用户信息
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404


# 创建新用户
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    if not new_user or 'name' not in new_user or 'email' not in new_user:
        return jsonify({'message': 'Bad request'}), 400
    new_user['id'] = max(user['id'] for user in users) + 1
    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(debug=True)
