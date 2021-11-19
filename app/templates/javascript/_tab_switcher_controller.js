Stimulus.register("tab-switcher", class extends Controller {
    static get targets() {
      return ["tabList"]
    }

  connect() {
    this.generate_tab_list();
    this.default_tab = this.list_all_tabs()[0].dataset.tab;
    this.activate_tab(this.default_tab);
  }
  
  generate_tab_list() {
    var html = ""
    this.list_all_tabs().forEach(tab => html += "<span class='tab-link ml-4 mr-4' data-tab-name=" + tab.dataset.tab + " data-action='click->tab-switcher#activate'>"+ tab.dataset.tab +"</span>" )

    this.tabListTarget.innerHTML = html
  }

  activate(event){
    this.activate_tab(event.target.dataset.tabName);
  }

  activate_tab(tabName){
    this.list_all_tabs().forEach(tab => tab.dataset.active = "false")
    var activated_tab = document.querySelector("[data-tab="+ tabName +"]");
    activated_tab.dataset.active = "true";

    this.list_all_tab_links().forEach(tab => tab.dataset.active = "false")
    var activated_tab_link = document.querySelector("[data-tab-name="+ tabName +"]");
    activated_tab_link.dataset.active = "true";
  }

  list_all_tabs() {
    return document.querySelectorAll(".tab")
  }

  list_all_tab_links() {
    return document.querySelectorAll(".tab-link")
  }

})