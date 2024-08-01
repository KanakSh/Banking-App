from flask import Flask, jsonify, request

app = Flask(__name__)



accounts={}

#creating a new account and giving error if it already exists

@app.route('/accounts', methods=['POST'])
def create_account():
    account_id = request.json.get('account_id')
    initial_balance = request.json.get('initial_balance', 0)
    if account_id in accounts:
        return jsonify({'message': 'Account already exists'}), 400
    accounts[account_id] = {'balance': initial_balance}
    return jsonify({'message': 'Account created', 'account': accounts[account_id]}), 201

#getting the account details one at a time

@app.route('/accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    account = accounts.get(account_id)
    if not account:
        return jsonify({'message': 'Account not found'}), 404
    return jsonify({'account': account}), 200

#getting all the account details at once

@app.route('/accounts/getall', methods=['GET'])
def get_all_account():
    return jsonify(accounts), 200

#for depositing, adding into existing bank account

@app.route('/accounts/<account_id>/<int:amount>', methods=['PATCH'])
def deposit_money(account_id, amount):
    account = accounts.get(account_id)

    if not account:
        return jsonify({'message': 'Account not found'}), 404

    account['balance']+=amount
    return jsonify({'account': account}), 200

#for deleting an account
@app.route('/accounts/delete/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = accounts.get(account_id)
    if not account:
        return jsonify({'message': 'Account not found'}), 404
    del accounts[account_id]
    #return jsonify({account_id: 'succesfully deleted'}), 200
    return f'sucssesfuly deleted account_id : {account_id}'



if __name__ == "__main__":
    app.run(debug=True)
