import {GenericApi} from "./GenericApi.js";

export class InstructorApi extends GenericApi {
  constructor(base_url) {
    super(base_url);
  }
  get_attendances(instructor_id, course_id) {
    return super.send({
      url: `${this.base_url}/${instructor_id}/courses/${course_id}/summary/`,
      method: 'GET',
    });
  }
  get_courses_student(instructor_id, course_id) {
    return super.send({
      url: `${this.base_url}/${instructor_id}/courses/${course_id}/students/`,
      method: 'GET',
    });
  }
  get_course_student_view(instructor_id, course_id, student_id) {
    return super.send({
      url: `${this.base_url}/${instructor_id}/courses/${course_id}/students/${student_id}/attendances`,
      method: 'GET',
    });
  }
}