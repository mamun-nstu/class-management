import {BaseApi} from "./BaseApi";

export class StudentApi extends BaseApi{
    static base_url() {
        return "/api/students";
    }
    static get_all(){
      return this.get(this.base_url());
    }
    static add(data){
      return this.post(this.base_url(), data);
    }
    static add(data){
      return this.post(this.base_url(), data);
    }
}