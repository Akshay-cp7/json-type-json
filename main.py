from odoo import http
from odoo.http import request

class MyApiController(http.Controller):
    
    @http.route('/api/v1/students', type='json', auth='public', methods=['GET'], csrf=False)
    def get_students(self, **kwargs):
        """
        Fetches a list of students
        """
        students = request.env['collage.student'].search([])  # Query all students
        student_data = []
        for student in students:
            student_data.append({
                'id': student.id,
                'name': student.name,
                'date_of_birth': student.date_of_birth,
                'gender': student.gender,
                'dept': student.dept,
            })
        return {'students': student_data}
