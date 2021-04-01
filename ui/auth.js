class Auth extends HTMLElement {
  getUser() {
    const value = window.localStorage.getItem("mfe-auth-user") || "{}";
    return JSON.parse(value);
  }

  setUser(value) {
    window.localStorage.setItem("mfe-auth-user", JSON.stringify(value))
    if (this.isAuthenticated()) {
      this.querySelector("form.login-form").style.display = "none";
      this.querySelector("div.logout-username").innerText = this.getUser().username;
      this.querySelector("form.logout-form").style.display = "inherit";
    } else {
      this.querySelector("form.login-form").style.display = "inherit";
      this.querySelector("div.logout-username").innerText = "";
      this.querySelector("form.logout-form").style.display = "none";
    }
    this.dispatchEvent(new CustomEvent('mfe-auth-changed', {
      bubbles: true,
    }));
  }

  connectedCallback() {
    this.innerHTML = `
      <div class="mfe-auth">
        <form class="login-form" style="display:inherit;">
          <div class="login-username">
            <div>Username</div>
            <div>
              <input
                  type="text"
                  name="username"
                  onChange={this.handleUpdate}
              />
            </div>
          </div>
          <div class="login-password">
            <div>Password</div>
            <div>
              <input
                  type="password"
                  name="password"
                  onChange={this.handleUpdate}
              />
            </div>
          </div>
          <div class="login-submit">
            <input type="submit" value="Log In" />
          </div>
        </form>
        <form class="logout-form" style="display:none;">
          <div class="logout-username"></div>
          <div class="logout-submit">
            <input type="submit" value="Log Out" />
          </div>
        </form>
      </div>
    `;
    this.querySelector("form.login-form").addEventListener("submit", this.login.bind(this));
    this.querySelector("form.logout-form").addEventListener("submit", this.logout.bind(this));
    this.setUser(this.getUser()); // Get the current value to see which form to display
  }
  
  disconnectedCallback() {
    this.querySelector("form.login-form").removeEventListener("submit", this.login.bind(this));
    this.querySelector("form.logout-form").removeEventListener("submit", this.logout.bind(this));
  }

  login(event) {
    event.preventDefault();
    event.stopPropagation();
    const form = event.currentTarget;
    const data = new URLSearchParams(new FormData(form));
    const url =  "api/v1/users/";
    fetch(`${url}login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: data
    })
      .then(response => response.json())
      .then((data) => this.setUser(data.success.user))
      .catch((error) => window.alert(error));
    this.querySelector("form.login-form input[type='password']").value = "";
  }
  
  isAuthenticated() {return this.getUser().authenticated ? true : false;}

  logout(event) {
    event.preventDefault();
    event.stopPropagation();
    const url =  "api/v1/users/";
    fetch(`${url}logout/`, {
      method: "POST", 
    })
      .then(response => response.json())
      .then((data) => this.setUser(data.success.user))
      .catch((error) => window.alert(error));
  }
}

window.customElements.define("mfe-auth", Auth);
console.log("mfe-auth");
window.addEventListener('mfe-auth-changed', (event) => console.log(`mfe-auth-changed: ${event.target.getUser().username ? event.target.getUser().username : ""}`));
