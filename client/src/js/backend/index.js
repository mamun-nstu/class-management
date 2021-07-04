import {BaseApi} from "./BaseApi";

class BackendApi {
  constructor() {
    this.generic = new BaseApi('');
    this.student = new BaseApi("/api/students");
  }
}

export default new BackendApi();