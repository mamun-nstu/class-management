import axios from 'axios';

export class BaseApi {
  constructor(base_url) {
    this.base_url = base_url;
  }

  send(config) {
    config.method = config.method || 'GET';
    config.url = config.url || this.base_url;
    console.debug('Url', config.url);
    return axios(config);
  }

  get_all(url = this.base_url, query= {}) {
    const config = {};
    config.method = 'GET';
    config.url = url;
    config.query = query;
    return this.send(config);
  }

  post(config) {
    config.method = 'POST';
    config.url = config.url || this.base_url;
    return this.send(config);
  }
  make_url(url, id){
    return `${url}/${id}`
  }
  get(config) {
    config.method = 'GET';
    config.url = config.url || this.base_url;
    return this.send(config);
  }
  put(config) {
    config.method = 'PUT';
    config.url = config.url || this.base_url;
    return this.send(config);
  }
  delete(config) {
    config.method = 'DELETE';
    config.url = config.url || this.base_url;
    return this.send(config);
  }
}