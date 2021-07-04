import axios from 'axios';

export class BaseApi {
  constructor(base_url) {
    this.base_url = base_url;
  }

  send(url, method = 'GET', data) {
    console.debug('Url', url);
    return axios({
      method,
      url,
      data,
    });
  }

  get_all(url = this.base_url) {
    return this.send(url, 'get');
  }

  post(url = this.base_url, data) {
    return this.send(url, 'post', data);
  }
  make_url(url, id){
    return `${url}/${id}`
  }
  get(url = this.base_url, id) {
    return this.send(this.make_url(url, id), 'get');
  }
  put(url = this.base_url, id, data) {
    return this.send(this.make_url(url, id), 'put', data);
  }
  delete(url = this.base_url, id) {
    return this.send(this.make_url(url, id), 'delete');
  }
}