import { computed, inject, Injectable, signal } from '@angular/core';
import { PRODUCTS } from '../../assets/products';
import { Product } from '../models/product.model';
import { StorageService } from './storage-service';
import { single } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ProductService {

  storageService: StorageService = inject(StorageService);

  productListSignal = this.storageService.productList;

  activeFilters = signal<string[]>([]);

  filteredProductList = computed(() =>
    this.productListSignal().filter(
      prod => this.activeFilters().every(filt => Object.values(prod.category).includes(filt)))
  );

  filterProducts(newFilters: string[]) {
    this.activeFilters.set(newFilters);
  }

  likeProduct(productInstance: Product) {
    const list = this.storageService.productList();

    const id = list.findIndex(prod => prod.id === productInstance.id);

    const entry = list[id];
    list[id] = { ...entry, likes: entry.likes + 1 };
    this.storageService.update(list);

  }

  getLikesInfo(productInstance: Product) {
    const list = this.storageService.productList();
    const id = list.findIndex(prod => prod.id === productInstance.id);
    return list[id].likes;
  }

  deleteProduct(productId: number) {
    this.storageService.update(
      this.productListSignal().filter(prod => prod.id !== productId)
    );
  }



}

