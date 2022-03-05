import {GenericApi} from "./GenericApi.js";

export class StudentApi extends GenericApi {
  constructor(base_url) {
    super(base_url);
  }
  get_attendances(student_id, course_id) {
    return super.send({
      url: `${this.base_url}/${student_id}/courses/${course_id}/attendances/`,
      method: 'GET',
    });
  }
  get_attendance_summary(student_id) {
    return super.send({
      url: `${this.base_url}/${student_id}/attendance_summary/`,
      method: 'GET',
    });
  }
}