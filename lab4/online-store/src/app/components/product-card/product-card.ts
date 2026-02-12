import { Component, Input, signal } from '@angular/core';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-card',
  imports: [],
  templateUrl: `./product-card.html`,
  styleUrl: `./product-card.css`,
})
export class ProductCard {
  @Input({ required: true }) product!: Product;
  currentImageId = signal(0);

  increment() {
    this.currentImageId.update((oldValue) => {
      let newValue = oldValue + 1;
      newValue %= this.product.images.length;
      return newValue;
    });
  }

  getWhatsappRedirectUrl() {
    return "https://wa.me/?text=Check out this product: " + this.product.link;
  }

}
