{% extends "layout.html" %}
{% block content %}

<section class="register_section_css">
  <div class="container">
          <div class="box">

          </div>
          <div class="box">
              {% with messages = get_flashed_messages(with_categories=true) %}
                  {% if messages %}
                      {% for category, message in messages %}
                          <div class="alert alert-{{ category }}">
                              {{ message }}
                          </div> 
                      {% endfor %}
                  {% endif %}
              {% endwith %}
              <form method="POST" action="">
                  {{ form.hidden_tag() }}
                      <fieldset class="form-group">
                          <legend class="border-bottom mb-4">Log In</legend>
                          <div class="form-group">
                              {{ form.email.label(class="form-control-label") }}
                              {% if form.email.errors %}
                                  {{ form.email(class="form-control form-control-lg is-invalid") }}
                                  <div class="invalid-feedback">
                                      {% for error in form.email.errors %}
                                          <span>{{ error }}</span>
                                      {% endfor %}
                                  </div>
                              {% else %}
                                  {{ form.email(class="form-control form-control-lg") }}
                              {% endif %}
                          </div>
                          <div class="form-group">
                              {{ form.password.label(class="form-control-label") }}
                              {% if form.password.errors %}
                                  {{ form.password(class="form-control form-control-lg is-invalid") }}
                                  <div class="invalid-feedback">
                                      {% for error in form.password.errors %}
                                          <span>{{ error }}</span>
                                      {% endfor %}
                                  </div>
                              {% else %}
                                  {{ form.password(class="form-control form-control-lg") }}
                              {% endif %}
                          </div>
                          <div class="form-check">
                              {{ form.remember(class="form-check-input",style="text-align: left;") }}
                              {{ form.remember.label(class="form-check-label",style="text-align: left;") }}
                          </div>
                      </fieldset>
                      </br>
                      <div class="form-group">
                          {{ form.submit(class="btn btn-outline-info") }}
                      </div>
              </form>
              </br>
              <div class="border-top pt-3">
                  <small>
                      Need An Account? <a class="ml-2" href="{{ url_for('users.register') }}">Register</a>
                  </small>
              </div>

          </div>
          <div class="box">

          </div>
  </div>
</section>

        
{% endblock content %}
