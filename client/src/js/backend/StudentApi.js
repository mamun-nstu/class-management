import {GenericApi} from "./GenericApi.js";

export class StudentApi extends GenericApi {
  constructor(base_url) {
    super(base_url);
  }
  get_attendances(course_id) {
    return super.send({
      url: `${this.base_url}/attendances/courses/${course_id}/`,
      method: 'GET',
    });
  }
  get_attendance_summary() {
    return super.send({
      url: `${this.base_url}/attendance_summary/`,
      method: 'GET',
    });
  }
}