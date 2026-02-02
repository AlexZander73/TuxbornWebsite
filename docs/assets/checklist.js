(() => {
  const storagePrefix = "checklist:";

  const getKey = (pageId, rowIndex) => `${storagePrefix}${pageId}:${rowIndex}`;

  const getChecked = (pageId, rowIndex) => {
    try {
      return localStorage.getItem(getKey(pageId, rowIndex)) === "1";
    } catch {
      return false;
    }
  };

  const setChecked = (pageId, rowIndex, value) => {
    try {
      localStorage.setItem(getKey(pageId, rowIndex), value ? "1" : "0");
    } catch {
      // no-op
    }
  };

  const updateProgress = (container, pageId, totalRows) => {
    const progress = container.closest(".md-typeset")?.querySelector(".checklist-progress");
    if (!progress) return;
    let completed = 0;
    for (let i = 0; i < totalRows; i += 1) {
      if (getChecked(pageId, i)) completed += 1;
    }
    const percent = totalRows === 0 ? 0 : Math.round((completed / totalRows) * 100);
    const bar = progress.querySelector(".checklist-progress__bar span");
    const label = progress.querySelector(".checklist-progress__label");
    if (bar) bar.style.width = `${percent}%`;
    if (label) label.textContent = `${percent}% complete (${completed}/${totalRows})`;
  };

  const buildSummary = (container, data) => {
    if (!data.include_tab_column) return;
    const summary = container.closest(".md-typeset")?.querySelector(".checklist-summary");
    if (!summary) return;

    const tabIndex = data.headers.findIndex((h) => h.toLowerCase() === "tab");
    if (tabIndex === -1) return;

    const totals = new Map();
    data.rows.forEach((row, idx) => {
      const tab = row[tabIndex] || "Other";
      const entry = totals.get(tab) || { total: 0, done: 0 };
      entry.total += 1;
      if (getChecked(data.page_id, idx)) entry.done += 1;
      totals.set(tab, entry);
    });

    summary.innerHTML = "";
    const list = document.createElement("div");
    list.className = "checklist-summary__list";

    Array.from(totals.entries())
      .sort((a, b) => a[0].localeCompare(b[0]))
      .forEach(([tab, stats]) => {
        const percent = stats.total === 0 ? 0 : Math.round((stats.done / stats.total) * 100);
        const item = document.createElement("div");
        item.className = "checklist-summary__item";
        item.innerHTML = `
          <div class="checklist-summary__title">${tab}</div>
          <div class="checklist-summary__bar"><span style="width:${percent}%"></span></div>
          <div class="checklist-summary__meta">${percent}% (${stats.done}/${stats.total})</div>
        `;
        list.appendChild(item);
      });

    summary.appendChild(list);
  };

  const buildTable = (container, data) => {
    container.innerHTML = "";

    const table = document.createElement("table");
    table.className = "md-typeset checklist-table__table";

    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");

    const doneHeader = document.createElement("th");
    doneHeader.textContent = "Done";
    headerRow.appendChild(doneHeader);

    data.headers.forEach((header) => {
      const th = document.createElement("th");
      th.textContent = header;
      headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");
    data.rows.forEach((row, rowIndex) => {
      const tr = document.createElement("tr");

      const doneCell = document.createElement("td");
      doneCell.className = "checklist-table__done";
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.checked = getChecked(data.page_id, rowIndex);
      checkbox.addEventListener("change", () => {
        setChecked(data.page_id, rowIndex, checkbox.checked);
        updateProgress(container, data.page_id, data.rows.length);
        buildSummary(container, data);
      });
      doneCell.appendChild(checkbox);
      tr.appendChild(doneCell);

      row.forEach((cell) => {
        const td = document.createElement("td");
        td.textContent = cell;
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);

    container.appendChild(table);
  };

  const initTables = () => {
    document.querySelectorAll(".checklist-table").forEach((container) => {
      const raw = container.getAttribute("data-checklist");
      if (!raw) return;
      const data = JSON.parse(raw);
      buildTable(container, data);

      const wrapper = container.closest(".md-typeset") || document;
      const searchInput = wrapper.querySelector(".checklist-search");
      const filtersWrapper = wrapper.querySelector(".checklist-filters");
      const table = container.querySelector("table");
      if (!table) return;

      updateProgress(container, data.page_id, data.rows.length);
      buildSummary(container, data);

      const rows = Array.from(table.querySelectorAll("tbody tr"));
      const headers = Array.from(table.querySelectorAll("thead th")).map((th) => th.textContent);

      const columnFilters = headers
        .map((header, index) => ({ header, index }))
        .filter(({ header }) => header && header.toLowerCase() !== "tab" && header !== "Done");

      const filterControls = [];
      columnFilters.forEach(({ header, index }) => {
        const values = new Set();
        rows.forEach((row) => {
          const cell = row.children[index];
          if (cell && cell.textContent.trim()) values.add(cell.textContent.trim());
        });
        if (values.size === 0 || values.size > 30) return;

        const select = document.createElement("select");
        select.setAttribute("data-filter-index", String(index));
        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.textContent = `${header}: All`;
        select.appendChild(defaultOption);

        Array.from(values)
          .sort((a, b) => a.localeCompare(b))
          .forEach((value) => {
            const option = document.createElement("option");
            option.value = value;
            option.textContent = value;
            select.appendChild(option);
          });

        filtersWrapper?.appendChild(select);
        filterControls.push(select);
      });

      const applyFilters = () => {
        const query = searchInput?.value.trim().toLowerCase() || "";
        const selections = filterControls.map((select) => ({
          index: Number(select.getAttribute("data-filter-index")),
          value: select.value,
        }));

        rows.forEach((row) => {
          const text = row.textContent.toLowerCase();
          const matchesQuery = !query || text.includes(query);
          const matchesFilters = selections.every(({ index, value }) => {
            if (!value) return true;
            const cell = row.children[index];
            return cell && cell.textContent.trim() === value;
          });
          row.style.display = matchesQuery && matchesFilters ? "" : "none";
        });
      };

      if (searchInput) {
        searchInput.addEventListener("input", applyFilters);
      }
      filterControls.forEach((select) => select.addEventListener("change", applyFilters));
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTables);
  } else {
    initTables();
  }
})();
