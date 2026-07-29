// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-首页",
          title: "首页",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/home-zh/";
          },
        },{id: "nav-home",
          title: "Home",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/";
          },
        },{id: "nav-科研",
          title: "科研",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research-zh/";
          },
        },{id: "nav-research",
          title: "Research",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-团队",
          title: "团队",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/team-zh/";
          },
        },{id: "nav-team",
          title: "Team",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/team/";
          },
        },{id: "nav-成果",
          title: "成果",
          description: "*代表共同第一作者，†代表共同通讯作者。",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications-zh/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "* co-first author &amp;nbsp;&amp;nbsp; † co-corresponding author",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "news-叶智文实验室将于2026年7月20日在深圳医学科学院-smart-神经调控与认知研究所-inc-正式成立",
          title: '🎉 叶智文实验室将于2026年7月20日在深圳医学科学院（SMART）神经调控与认知研究所（INC）正式成立！🎉',
          description: "",
          section: "News",},{id: "news-ye-lab-is-opening-at-the-institute-of-neuromodulation-and-cognition-inc-smart-on-july-20-2026",
          title: '🎉🎉Ye Lab is opening at the Institute of Neuromodulation and Cognition (INC), SMART,...',
          description: "",
          section: "News",},{id: "news-欢迎来自ucl的访问学生赖思澄加入实验室进行暑期研究",
          title: '🎉🎉欢迎来自UCL的访问学生赖思澄加入实验室进行暑期研究。',
          description: "",
          section: "News",},{id: "news-welcome-visiting-student-sicheng-lai-from-ucl-joining-the-lab-for-the-summer",
          title: '🎉🎉Welcome visiting student Sicheng Lai from UCL joining the lab for the summer....',
          description: "",
          section: "News",},{id: "news-欢迎研究助理殷伟伟加入实验室-此前为清华大学郭增才教授实验室研究助理",
          title: '🎉🎉欢迎研究助理殷伟伟加入实验室，此前为清华大学郭增才教授实验室研究助理。',
          description: "",
          section: "News",},{id: "news-welcome-research-assistant-weiwei-yin-joining-the-lab-previously-a-research-assistant-from-the-lab-of-prof-zengcai-guo-from-tsinghua-university",
          title: '🎉🎉Welcome Research Assistant Weiwei Yin joining the lab, previously a Research Assistant from...',
          description: "",
          section: "News",},{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/zhiwen10", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/zhiwen-ye-36734a111", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0003-4311-1037", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=TsbqbhEAAAAJ", "_blank");
        },
      },];
