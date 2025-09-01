from tabulate import tabulate
from Teacher import Teacher
from Student_List import StudentList
from File import FileHandler
from flask import request 


class AppController:
    
    
    
    def __init__(self, teacher=None, student_list=None):
        self.teacher = teacher
        self.student_list = student_list
    
    def run(self):
        Student=input("Enter anything to start:")
        if Student=="k":
            teacher = Teacher("Dr. Humera Tariq", "CS-352")
            students = StudentList()
            
            for s in FileHandler.load_students("results.csv"):
                students.add_student(s)

            app = AppController(teacher, students)
            app.display_results()

            

        else:
            teacher = Teacher("Dr. Humera Tariq", "CS-352")
            students = StudentList()
            
            for s in FileHandler.load_students("results.csv"):
                students.add_student(s)

            app = AppController(teacher, students)
            app.position()
            while (True):
                
                seat = input("\nEnter Seat No to search: ")
                if(seat=="exit" or seat=="Exit" or seat=="EXIT"):
                    break
                app.search_student(seat)
        
    def position(self):
        print("=" * 92)
        print("OOPs Mid Term Results (Python)".center(70))
        print("=" * 92)
        print(f"Teacher: {self.teacher.name}")
        print(f"Course Code: {self.teacher.course_code}\n")
        print("Developed By: Behroz, Fatima Shahzad, Asad, Rizwan, Syeda Kaneez Fatima, Zain.")
        print("=" * 92)

        self.assign_ranks()

        headers = ["Rank", "Seat No", "Name", "Q1", "Q2", "Q3", "Q4", "Q5", "Total"]
        table = []
        for s in self.ranked_students:
            rank_display = f"{s.rank}{'*' if s.tie else ''}"
            if s.rank==1 or s.rank==2 or s.rank==3 or s.rank==4:
                table.append([rank_display, s.seat_no, s.name, s.q1, s.q2, s.q3, s.q4, s.q5, s.total])

        print(tabulate(table, headers, tablefmt="grid", numalign="center", stralign="center"))
        


    def assign_ranks(self):
        students = sorted(self.student_list.get_all_students(), key=lambda s: s.total, reverse=True)

        current_rank = 1
        students[0].rank = current_rank
        students[0].tie = False

        for i in range(1, len(students)):
            if students[i].total == students[i - 1].total:
                students[i].rank = students[i - 1].rank
                students[i].tie = True
                students[i - 1].tie = True
            else:
                students[i].rank = students[i - 1].rank + 1
                students[i].tie = False

        self.ranked_students = students

    def display_results(self):
        print("=" * 92)
        print("OOPs Mid Term Results (Python)".center(70))
        print("=" * 92)
        print(f"Teacher: {self.teacher.name}")
        print(f"Course Code: {self.teacher.course_code}\n")
        print("Developed By: Behroz, Fatima Shahzad, Asad, Rizwan, Syeda Kaneez Fatima, Zain.")
        print("=" * 92)

        self.assign_ranks()

        headers = ["Rank", "Seat No", "Name", "Q1", "Q2", "Q3", "Q4", "Q5", "Total"]
        table = []
        for s in self.ranked_students:
            rank_display = f"{s.rank}{'*' if s.tie else ''}"
            
            table.append([rank_display, s.seat_no, s.name, s.q1, s.q2, s.q3, s.q4, s.q5, s.total])

        print(tabulate(table, headers, tablefmt="grid", numalign="center", stralign="center"))


    def search_student(self, seat_no):
        student = self.student_list.search_by_seat(seat_no)
        if student:
            print("\nSearch Result:")
            print(f"Seat No: {student.seat_no}")
            print(f"Name: {student.name}")
            print(f"Q1: {student.q1}, Q2: {student.q2}, Q3: {student.q3}, Q4: {student.q4}, Q5: {student.q5}")
            print(f"Total: {student.total}, Rank: {student.rank}{'*' if student.tie else ''}")
        else:
            print("\nStudent not found.")


    
    
    
    
    
    
    def _wrap_page(self, body_html, title="OOPs Mid Term Results (Python)"):
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8"/>
            <title>{title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 24px; }}
                .container {{ max-width: 1000px; margin: 0 auto; }}
                h1, h2, h3 {{ text-align: center; }}
                .meta {{ text-align:center; margin-bottom: 16px; }}
                table {{ border-collapse: collapse; margin: 12px auto; width: 100%; }}
                th, td {{ border: 1px solid #333; padding: 8px; text-align: center; }}
                th {{ background-color: #f2f2f2; }}
                .form {{ text-align:center; margin: 20px 0; }}
                input[type="text"] {{ padding: 8px; width: 260px; }}
                button {{ padding: 8px 14px; cursor: pointer; }}
                .notfound {{ text-align:center; margin-top: 10px; }}
                .muted {{ color: #666; font-size: 0.9rem; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>OOPs Mid Term Results (Python)</h1>
                <div class="meta">
                    <div>Teacher: <b>{self.teacher.name}</b> &nbsp;|&nbsp; Course Code: <b>{self.teacher.course_code}</b></div>
                    <div class="muted">Developed By: Behroz, Fatima Shahzad, Asad, Rizwan, Syeda Kaneez Fatima, Zain.</div>
                </div>
                {body_html}
            </div>
        </body>
        </html>
        """

    def top_positions_html(self, top_n=4):
        self.assign_ranks()
        headers = ["Rank", "Seat No", "Name", "Q1", "Q2", "Q3", "Q4", "Q5", "Total"]
        rows = []
        for s in self.ranked_students[:top_n]:
            rank_display = f"{s.rank}{'*' if s.tie else ''}"
            rows.append([rank_display, s.seat_no, s.name, s.q1, s.q2, s.q3, s.q4, s.q5, s.total])
        table_html = tabulate(rows, headers, tablefmt="html", numalign="center", stralign="center")
        return f"<h2>Top {top_n}</h2>{table_html}"

    def all_results_html(self):
        self.assign_ranks()
        headers = ["Rank", "Seat No", "Name", "Q1", "Q2", "Q3", "Q4", "Q5", "Total"]
        rows = []
        for s in self.ranked_students:
            rank_display = f"{s.rank}{'*' if s.tie else ''}"
            rows.append([rank_display, s.seat_no, s.name, s.q1, s.q2, s.q3, s.q4, s.q5, s.total])
        table_html = tabulate(rows, headers, tablefmt="html", numalign="center", stralign="center")
        return f"<h2>All Results</h2>{table_html}"

    def search_form_html(self, prefill=""):
        return f"""
        <div class="form">
            <form action="/" method="get">
                <input type="text" name="seat" placeholder="Enter Seat No..." value="{prefill}"/>
                <button type="submit">Search</button>
            </form>
        </div>
        """

    def search_student_html(self, seat_no):
        student = self.student_list.search_by_seat(seat_no)
        if not student:
            return f'<div class="notfound">No student found for Seat No <b>{seat_no}</b>.</div>'

        headers = ["Seat No", "Name", "Q1", "Q2", "Q3", "Q4", "Q5", "Total", "Rank"]
        rank_display = f"{student.rank}{'*' if getattr(student, 'tie', False) else ''}"
        row = [[student.seat_no, student.name, student.q1, student.q2, student.q3, student.q4, student.q5, student.total, rank_display]]
        table_html = tabulate(row, headers, tablefmt="html", numalign="center", stralign="center")
        return f"<h2>Search Result</h2>{table_html}"

    def page_with_search(self, seat_query=None, show_all=False):
        body = self.search_form_html(prefill=seat_query or "")
        body += self.top_positions_html(top_n=4)
        if show_all:
            body += self.all_results_html()
        if seat_query:
            body += self.search_student_html(seat_query)
        return self._wrap_page(body)
    
    def run_web(self):
        # simulate "if Student == 'k'" → show_all
        # otherwise → show top positions
        mode = request.args.get("mode", "positions")  # default to positions
        seat = request.args.get("seat")

        show_all = (mode == "all")

        return self.page_with_search(seat_query=seat, show_all=show_all)

    # -----------------------------
    # Existing page builder
    # -----------------------------
    def page_with_search(self, seat_query=None, show_all=False):
        body = self.search_form_html(prefill=seat_query or "")

        # ✅ if/else logic mirrored from console:
        if show_all:
            body += self.all_results_html()
        else:
            body += self.top_positions_html(top_n=4)

        if seat_query:
            body += self.search_student_html(seat_query)

        # Add navigation links like console choices
        body += """
        
        """

        return self._wrap_page(body)
