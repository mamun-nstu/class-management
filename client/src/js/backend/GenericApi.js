import {BaseApi} from "./BaseApi";

export class GenericApi extends BaseApi {
  constructor(base_url) {
    super(base_url);
  }

  get_all(query = {}) {
    return super.get_all(this.base_url, query);
  }

  delete(id) {
    return super.delete({
      url: this.make_url(this.base_url, id)
    });
  }

  get(id) {
    return super.get({
      url: this.make_url(this.base_url, id)
    });
  }

  // add(data) {
  //   return this.post(base_url, data);
  // }
}