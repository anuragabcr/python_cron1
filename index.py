from flask import Flask, request, jsonify
import schedule
import time

from actions import find_documents, create_document, update_document, delete_document 

def job():
    print("Hello")
    cursor = find_documents("Anurag", "students", {})
    for document in cursor:
        print(document)

schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(59)


app = Flask(__name__)

DATABASE = "testDB"
COLLECTION = "test"

# Create
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    if data:
        inserted = create_document(DATABASE, COLLECTION, data)
        return jsonify({'message': 'Document created successfully', 'id': str(inserted.inserted_id)}), 201
    else:
        return jsonify({'error': 'No data provided'}), 400

# Read
@app.route('/read', methods=['POST'])
def read():
    query = request.json
    result = find_documents(DATABASE, COLLECTION, query)
    return jsonify(result)

# Update
@app.route('/update/<string:id>', methods=['PUT'])
def update(id):
    data = request.json
    if data:
        updated = update_document(DATABASE, COLLECTION, id, data)
        if updated.modified_count:
            return jsonify({'message': 'Document updated successfully'}), 200
        else:
            return jsonify({'error': 'Document not found'}), 404
    else:
        return jsonify({'error': 'No data provided'}), 400

# Delete
@app.route('/delete/<string:id>', methods=['DELETE'])
def delete(id):
    deleted = delete_document(DATABASE, COLLECTION, id)
    if deleted.deleted_count:
        return jsonify({'message': 'Document deleted successfully'}), 200
    else:
        return jsonify({'error': 'Document not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)