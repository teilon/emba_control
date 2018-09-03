from datetime import datetime


def create_product_set(data):
    # create new row in table ProductSet and return id
    product_set = 0
    return product_set


def get_current_product_set_id():
    # get current product set from storage db (id)
    return 0


def get_product_set_data(id):
    data = {}
    return data


def add_product_set(new_product_set):
    # add data to ProductSet and get id
    new_product_set_id = 0
    return new_product_set_id


def add_product_set(current_product_set_id, data_set_id):
    current_set = get_product_set_data(current_product_set_id)
    receipt_set = get_product_set_data(data_set_id)
    new_product_set = current_set + receipt_set
    new_product_set_id = add_product_set(new_product_set)
    return new_product_set_id


def create_new_product_set(data_set_id, status):
    current_product_set_id = get_current_product_set_id()
    if status == 'receipt':
        new_product_set_id = add_product_set(current_product_set_id, data_set_id)

    return new_product_set_id


def create_transaction(data_set_id, status):
    # add new row to Transaction
    current_data = datetime.now()
    current_user = 'admin'
    # Transaction.add(data_set_id, status, current_data, current_user)
    transaction_id = 0
    return transaction_id


def change_storage_set(new_product_set_id, transaction_id):
    # add new row to Storage
    pass


def start_transaction(data_set_id, status):
    new_product_set_id = create_new_product_set(data_set_id, status)
    transaction_id = create_transaction(data_set_id, status)
    change_storage_set(new_product_set_id, transaction_id)


def receipt(data):
    status = 'receipt'
    receipt_set_id = create_product_set(data)
    start_transaction(receipt_set_id, status)
