import {GenericApi} from "./GenericApi.js";

export class InstructorApi extends GenericApi {
  constructor(base_url) {
    super(base_url);
  }
  get_attendances(course_id) {
    return super.send({
      url: `${this.base_url}/summary/courses/${course_id}/`,
      method: 'GET',
    });
  }
  get_courses_student(course_id) {
    return super.send({
      url: `${this.base_url}/courses/${course_id}/students/`,
      method: 'GET',
    });
  }
  get_courses() {
    return super.send({
      url: `${this.base_url}/courses/`,
      method: 'GET',
    });
  }
  get_course_student_view(course_id, student_id) {
    return super.send({
      url: `${this.base_url}/attendances/courses/${course_id}/students/${student_id}/`,
      method: 'GET',
    });
  }
}