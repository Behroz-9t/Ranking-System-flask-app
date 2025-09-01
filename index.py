from flask import Flask, request, jsonify
from App_Controller import AppController
from Teacher import Teacher
from Student_List import StudentList
from File import FileHandler

app = Flask(__name__)

def build_controller():
    teacher = Teacher("Dr. Humera Tariq", "CS-352")
    students = StudentList()
    for s in FileHandler.load_students("results.csv"):
        students.add_student(s)
    return AppController(teacher, students)

@app.route("/", methods=["GET"])
def home():
    controller = build_controller()
    seat = request.args.get("seat", "").strip()

    if seat.lower() == "k":
        show_all = True
        seat_query = None
    else:
        show_all = request.args.get("all", "").lower() in ("1", "true", "yes")
        seat_query = seat or None

    return controller.page_with_search(seat_query=seat_query, show_all=show_all)

@app.route("/search/<seat_no>", methods=["GET"])
def search_by_path(seat_no):
    controller = build_controller()
    body = controller.search_form_html(prefill=seat_no)
    body += controller.search_student_html(seat_no)
    return controller._wrap_page(body, title=f"Search {seat_no}")

@app.route("/api/student/<seat_no>", methods=["GET"])
def api_student(seat_no):
    controller = build_controller()
    s = controller.student_list.search_by_seat(seat_no)
    if not s:
        return jsonify({"ok": False, "error": "not_found", "seat_no": seat_no}), 404
    return jsonify({
        "ok": True,
        "seat_no": s.seat_no,
        "name": s.name,
        "q1": s.q1, "q2": s.q2, "q3": s.q3, "q4": s.q4, "q5": s.q5,
        "total": s.total,
        "rank": getattr(s, "rank", None),
        "tie": getattr(s, "tie", False),
    })


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)