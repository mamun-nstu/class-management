import {BaseApi} from "./BaseApi";
import {StudentApi} from "./StudentApi.js";
import {GenericApi} from "./GenericApi.js";
import { InstructorApi } from "./InstructorApi";
import { AuthApi } from "./AuthApi";

class BackendApi {
  constructor() {
    this.generic = new BaseApi('');
    this.student = new StudentApi("/api/students");
    this.batch = new GenericApi("/api/batches");
    this.course = new GenericApi("/api/courses");
    this.instructor = new InstructorApi("/api/instructors");
    this.auth = new AuthApi("/api/auth/");
    this.others = new BaseApi('');
  }
}

export default new BackendApi();