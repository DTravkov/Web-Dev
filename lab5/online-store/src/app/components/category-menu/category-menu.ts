import { Component, effect, output, signal } from '@angular/core';
import { CategoryButton } from "../category-button/category-button";

@Component({
  selector: 'app-category-menu',
  imports: [CategoryButton],
  templateUrl: './category-menu.html',
  styleUrl: './category-menu.css',
})
export class CategoryMenu {
  filterList = signal<string[]>([]);
  filterEvent = output<string[]>();

  constructor() {
    effect(() => {
      this.filterEvent.emit(this.filterList());
    });
  }

  handleOptionEvent(eventName: string) {

    const filterName = eventName.split(':')[0];
    const eventType = eventName.split(':')[1];

    if (eventType === 'on' && !this.filterList().includes(filterName)) {
      this.filterList.update(arr => [...arr, filterName]);
    }
    if (eventType === 'off' && this.filterList().includes(filterName)) {
      this.filterList.update(arr => arr.filter(x => x !== filterName));
    }

  }
}
