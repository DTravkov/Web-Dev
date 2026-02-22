import { Injectable, signal } from '@angular/core';
import { PRODUCTS } from '../../assets/products';
import { Product } from '../models/product.model';

@Injectable({
  providedIn: 'root',
})
export class ProductService {

  allProducts = PRODUCTS;
  activeProducts = signal<Product[]>([]);

  deletedIds: number[] = [];


  filterProducts(filters: string[]) {
    const filtered = this.allProducts.filter(prod => {
      if (filters.every(filt => Object.values(prod.category).includes(filt))
        && !this.deletedIds.includes(prod.id)) {
        return true;
      }
      return false;
    }
    );
    this.activeProducts.set(filtered);

    return this.activeProducts;
  }

  deleteProduct(productId: number) {
    this.deletedIds.push(productId);
    this.activeProducts.set(
      this.activeProducts().filter(prod => !this.deletedIds.includes(prod.id))
    );
    return this.activeProducts;
  }



}
