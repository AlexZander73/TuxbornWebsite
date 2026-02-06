(() => {
  const palettes = [
    { name: "Dragonborn", icon: "pets", scheme: "default", primary: "brown", accent: "grey" },
    { name: "Imperial", icon: "security", scheme: "default", primary: "amber", accent: "deep-orange" },
    { name: "Stormcloaks", icon: "ac_unit", scheme: "default", primary: "blue", accent: "light-blue" },
    { name: "Thalmor", icon: "auto_awesome", scheme: "default", primary: "indigo", accent: "amber" },
    { name: "Dark Brotherhood", icon: "warning", scheme: "slate", primary: "red", accent: "red" },
    { name: "Dawnguard", icon: "local_fire_department", scheme: "default", primary: "red", accent: "amber" },
    { name: "Volkihar", icon: "bloodtype", scheme: "slate", primary: "deep-purple", accent: "red" },
    { name: "Thieves Guild", icon: "vpn_key", scheme: "default", primary: "brown", accent: "orange" },
    { name: "Companions", icon: "pets", scheme: "default", primary: "green", accent: "lime" },
    { name: "College of Winterhold", icon: "auto_fix_high", scheme: "default", primary: "cyan", accent: "teal" },
    { name: "Bards College", icon: "music_note", scheme: "default", primary: "pink", accent: "deep-orange" },
    { name: "Greybeards", icon: "terrain", scheme: "default", primary: "blue-grey", accent: "grey" },
    { name: "Blades", icon: "military_tech", scheme: "default", primary: "orange", accent: "deep-orange" },
    { name: "Forsworn", icon: "gavel", scheme: "slate", primary: "brown", accent: "red" },
    { name: "Vigilants", icon: "flare", scheme: "default", primary: "grey", accent: "amber" },
  ];

  const storageKey = "__palette";

  const getStored = () => {
    try {
      if (typeof window.__md_get === "function") {
        return window.__md_get(storageKey);
      }
      const raw = localStorage.getItem(storageKey);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  };

  const setStored = (palette) => {
    try {
      if (typeof window.__md_set === "function") {
        window.__md_set(storageKey, palette);
      } else {
        localStorage.setItem(storageKey, JSON.stringify(palette));
      }
    } catch {
      // no-op
    }
  };

  const setThemeColorMeta = () => {
    const color = getComputedStyle(document.body)
      .getPropertyValue("--md-primary-fg-color")
      .trim();
    if (!color) return;
    let meta = document.querySelector("meta[name='theme-color']");
    if (!meta) {
      meta = document.createElement("meta");
      meta.setAttribute("name", "theme-color");
      document.head.appendChild(meta);
    }
    meta.setAttribute("content", color);
  };

  const applyPalette = (palette) => {
    if (!palette) return;
    document.body.setAttribute("data-md-color-scheme", palette.scheme);
    document.body.setAttribute("data-md-color-primary", palette.primary);
    document.body.setAttribute("data-md-color-accent", palette.accent);
    setStored(palette);
    setThemeColorMeta();
  };

  const applyScheme = (scheme) => {
    const current = getStored() || {
      scheme: document.body.getAttribute("data-md-color-scheme"),
      primary: document.body.getAttribute("data-md-color-primary"),
      accent: document.body.getAttribute("data-md-color-accent"),
    };
    applyPalette({ ...current, scheme });
  };

  const getCurrentPalette = () => {
    const stored = getStored();
    if (stored) return stored;
    return {
      scheme: document.body.getAttribute("data-md-color-scheme"),
      primary: document.body.getAttribute("data-md-color-primary"),
      accent: document.body.getAttribute("data-md-color-accent"),
    };
  };

  const findPalette = (match) =>
    palettes.find(
      (palette) =>
        palette.scheme === match.scheme &&
        palette.primary === match.primary &&
        palette.accent === match.accent
    );

  const createIcon = (name) => {
    const span = document.createElement("span");
    span.className = "material-icons md-theme-icon";
    span.textContent = name;
    return span;
  };

  const buildSelector = () => {
    const navList = document.querySelector(".md-nav--primary .md-nav__list");
    if (!navList || document.getElementById("theme-selector")) return;

    const item = document.createElement("li");
    item.className = "md-nav__item md-theme-drawer";

    const title = document.createElement("span");
    title.className = "md-theme-drawer__title";
    title.textContent = "Website Themes";

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.id = "theme-selector";
    trigger.className = "md-theme-selector__trigger";
    trigger.setAttribute("aria-haspopup", "listbox");
    trigger.setAttribute("aria-expanded", "false");

    const icon = createIcon(palettes[0].icon);

    const label = document.createElement("span");
    label.className = "md-theme-selector__label";

    const chevron = document.createElement("span");
    chevron.className = "md-theme-selector__chevron";
    chevron.textContent = "▾";

    trigger.appendChild(icon);
    trigger.appendChild(label);
    trigger.appendChild(chevron);

    const menu = document.createElement("div");
    menu.className = "md-theme-selector__menu";
    menu.setAttribute("role", "listbox");
    menu.hidden = true;

    const setDisplay = (palette) => {
      icon.textContent = palette.icon;
      label.textContent = palette.name;
    };

    const closeMenu = () => {
      if (!menu.hidden) {
        menu.hidden = true;
        trigger.setAttribute("aria-expanded", "false");
      }
    };

    const menuHeader = document.createElement("div");
    menuHeader.className = "md-theme-selector__header";
    menuHeader.textContent = "Select a theme";
    menu.appendChild(menuHeader);

    palettes.forEach((palette) => {
      const option = document.createElement("button");
      option.type = "button";
      option.className = "md-theme-selector__option";
      option.setAttribute("role", "option");
      option.setAttribute("data-theme", palette.name);

      const optIcon = createIcon(palette.icon);
      const optLabel = document.createElement("span");
      optLabel.textContent = palette.name;

      option.appendChild(optIcon);
      option.appendChild(optLabel);
      option.addEventListener("click", () => {
        applyPalette(palette);
        setDisplay(palette);
        closeMenu();
        document.documentElement.dispatchEvent(new Event("theme-change"));
      });

      menu.appendChild(option);
    });

    const closeButton = document.createElement("button");
    closeButton.type = "button";
    closeButton.className = "md-theme-selector__close";
    closeButton.textContent = "Close";
    closeButton.addEventListener("click", closeMenu);
    menu.appendChild(closeButton);

    const schemeToggle = document.createElement("button");
    schemeToggle.type = "button";
    schemeToggle.className = "md-theme-drawer__toggle";
    schemeToggle.textContent = "Toggle Light/Dark";
    schemeToggle.addEventListener("click", () => {
      const current = getCurrentPalette();
      const nextScheme = current.scheme === "slate" ? "default" : "slate";
      applyScheme(nextScheme);
    });

    const current = getCurrentPalette();
    const match = findPalette(current) || palettes[0];
    setDisplay(match);
    setThemeColorMeta();

    trigger.addEventListener("click", (event) => {
      event.stopPropagation();
      const next = menu.hidden;
      menu.hidden = !next;
      trigger.setAttribute("aria-expanded", String(next));
    });

    document.addEventListener("click", closeMenu);

    item.appendChild(title);
    item.appendChild(trigger);
    item.appendChild(menu);
    item.appendChild(schemeToggle);
    navList.insertBefore(item, navList.firstChild);
  };

  const makeSiteTitleClickable = () => {
    const siteTitle = document.querySelector(".md-nav__title--site");
    if (siteTitle && !siteTitle.querySelector("a")) {
      const link = document.createElement("a");
      const headerHome = document.querySelector(".md-header__button.md-logo, .md-header__button.md-icon");
      link.href = headerHome?.getAttribute("href") || "./";
      link.textContent = siteTitle.textContent;
      siteTitle.textContent = "";
      siteTitle.appendChild(link);
    }
  };

  const initNavCollapse = () => {
    document.querySelectorAll(".md-nav__item--section").forEach((item) => {
      const toggle = item.querySelector("input.md-nav__toggle");
      const label = item.querySelector("label.md-nav__link");
      if (toggle && label && !label.dataset.bound) {
        label.dataset.bound = "1";
        label.addEventListener("click", (event) => {
          event.preventDefault();
          toggle.checked = !toggle.checked;
        });
      }
    });
  };

  const syncDesktopNavState = () => {
    if (!window.matchMedia("(min-width: 60em)").matches) return;
    document.querySelectorAll(".md-nav__item--section").forEach((item) => {
      const toggle = item.querySelector("input.md-nav__toggle");
      if (!toggle) return;
      const isActive = item.classList.contains("md-nav__item--active");
      toggle.checked = isActive;
    });
  };

  const init = () => {
    buildSelector();
    makeSiteTitleClickable();
    initNavCollapse();
    syncDesktopNavState();
    const observer = new MutationObserver(() => {
      buildSelector();
      makeSiteTitleClickable();
      initNavCollapse();
      syncDesktopNavState();
    });
    observer.observe(document.body, { childList: true, subtree: true });
    window.addEventListener("resize", syncDesktopNavState);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
