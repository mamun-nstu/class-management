import {BaseApi} from "./BaseApi";
import {StudentApi} from "./StudentApi.js";
import {GenericApi} from "./GenericApi.js";

class BackendApi {
  constructor() {
    this.generic = new BaseApi('');
    this.student = new StudentApi("/api/students");
    this.batch = new GenericApi("/api/batches");
    this.course = new GenericApi("/api/courses");
    this.instructor = new BaseApi("/api/instructors");
  }
}

export default new BackendApi();