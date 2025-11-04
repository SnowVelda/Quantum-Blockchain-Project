
from flask import Flask, request, jsonify
from wallet.wallet_manager import WalletManager

app = Flask(__name__)
wallet_manager = WalletManager(db_path='wallet/wallets.db')

@app.route('/wallets', methods=['POST'])
def create_wallet():
    wallet_id = wallet_manager.create_wallet()
    return jsonify({'wallet_id': wallet_id}), 201

@app.route('/wallets/<wallet_id>/balance', methods=['GET'])
def get_balance(wallet_id):
    balance = wallet_manager.get_balance(wallet_id)
    if balance is not None:
        return jsonify({'wallet_id': wallet_id, 'balance': balance})
    return jsonify({'error': 'Wallet not found'}), 404

@app.route('/wallets/<wallet_id>/deposit', methods=['POST'])
def deposit(wallet_id):
    data = request.get_json()
    amount = data.get('amount')
    if amount is None or not isinstance(amount, (int, float)) or amount <= 0:
        return jsonify({'error': 'Invalid amount'}), 400

    if wallet_manager.deposit(wallet_id, amount):
        return jsonify({'message': 'Deposit successful'})
    return jsonify({'error': 'Wallet not found or invalid amount'}), 404

@app.route('/wallets/<wallet_id>/withdraw', methods=['POST'])
def withdraw(wallet_id):
    data = request.get_json()
    amount = data.get('amount')
    if amount is None or not isinstance(amount, (int, float)) or amount <= 0:
        return jsonify({'error': 'Invalid amount'}), 400

    if wallet_manager.withdraw(wallet_id, amount):
        return jsonify({'message': 'Withdrawal successful'})
    return jsonify({'error': 'Wallet not found or insufficient funds'}), 400

@app.route('/wallets/<wallet_id>/transactions', methods=['GET'])
def get_transactions(wallet_id):
    transactions = wallet_manager.get_transactions(wallet_id)
    if transactions is not None:
        return jsonify({'wallet_id': wallet_id, 'transactions': transactions})
    return jsonify({'error': 'Wallet not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

