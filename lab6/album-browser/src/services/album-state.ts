import { effect, inject, Injectable, signal } from '@angular/core';
import { Album } from '../models/album';
import { AlbumService } from './album-service';
import { Photo } from '../models/photo';

@Injectable({
  providedIn: 'root',
})
export class AlbumState {
  albumService = inject(AlbumService);

  albumList = signal<Album[]>([]);
  photosList = signal<Photo[]>([]);

  selectedAlbum = signal<Album | null>(null);
  pendingId: number | null = null;

  constructor() {
    effect(() => {
      const albums = this.albumList();
      const id = this.pendingId;
      if (albums.length > 0 && id !== null) {
        this.selectAlbum(id);
        this.pendingId = null;
      }
    });
  }

  refresh() {
    this.albumService.getAlbums().subscribe(data => this.albumList.set(data));
  }

  setPendingId(id: number) {
    this.refresh();
    this.pendingId = id;
  }

  private selectAlbum(id: number) {
    this.selectedAlbum.set(this.albumList().find(album => album.id === id) ?? null);
    if (this.selectedAlbum() !== null) {
      this.albumService.getPhotos(this.selectedAlbum()!.id).subscribe(photos => this.photosList.set(photos));
    }
  }



}

