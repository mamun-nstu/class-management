import { BaseApi } from "./BaseApi";

export class AuthApi extends BaseApi {
  constructor(base_url) {
    super(base_url);
  }
  get_token(username) {
    return this.get({
      url: `${this.base_url}/token/`,
      params: {
        username
      },
    });
  }
  get_user_info() {
    return this.get({ url: `${this.base_url}/me/`, });
  }
}