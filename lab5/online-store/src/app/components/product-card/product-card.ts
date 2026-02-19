import { Component, input, signal, OnInit, output } from '@angular/core';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-card',
  imports: [],
  templateUrl: `./product-card.html`,
  styleUrl: `./product-card.css`,
})
export class ProductCard implements OnInit {
  product = input.required<Product>();
  currentImageId = signal(0);
  likeCount = signal<number>(0);
  deleteOutput = output<number>();
  ngOnInit() {
    this.likeCount.set(this.product().likes);
  }
  increment() {
    this.currentImageId.update((oldValue) => {
      let newValue = oldValue + 1;
      newValue %= this.product().images.length;
      return newValue;
    });
  }

  deleteEvent() {
    this.deleteOutput.emit(this.product().id);
  }

  incrementLike() {
    this.likeCount.update(val => val + 1);
  }

  getWhatsappRedirectUrl() {
    return "https://wa.me/?text=Check out this product: " + this.product().link;
  }

}
