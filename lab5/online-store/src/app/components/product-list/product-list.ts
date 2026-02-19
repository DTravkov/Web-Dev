import { Component, input, output } from '@angular/core';
import { ProductCard } from '../product-card/product-card';
import { PRODUCTS } from '../../../assets/products';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-list',
  imports: [ProductCard],
  templateUrl: `./product-list.html`,
  styleUrl: `./product-list.css`,
})
export class ProductList {
  products = input.required<Product[]>();

  deleteOutput = output<number>();

  deleteEvent(productId: number) {
    this.deleteOutput.emit(productId);
  }

}
