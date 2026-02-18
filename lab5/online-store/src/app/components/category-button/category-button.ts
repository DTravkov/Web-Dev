import { Component, Input, input, output, signal } from '@angular/core';

@Component({
  selector: 'app-category-button',
  imports: [],
  templateUrl: './category-button.html',
  styleUrl: './category-button.css',
})
export class CategoryButton {
  buttonText = input.required<string>();
  buttonOption = input.required<string>();
  optionEvent = output<string>();
  isActive = signal<boolean>(false);
  toggleOption() {
    if (this.isActive()) {
      this.isActive.update(a => !a);
      this.optionEvent.emit(this.buttonOption() + ":off");
    } else {
      this.isActive.update(a => !a);
      this.optionEvent.emit(this.buttonOption() + ":on");
    }

    return;
  }
}
