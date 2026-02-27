import { effect, inject, Injectable, input, signal } from '@angular/core';
import { Album } from '../models/album';
import { AlbumService } from './album-service';
import { Photo } from '../models/photo';
import { finalize } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AlbumState {
  albumService = inject(AlbumService);

  albumList = signal<Album[]>([]);
  photosList = signal<Photo[]>([]);

  selectedAlbum = signal<Album | null>(null);
  pendingId: number | null = null;

  isFetchingData = signal<boolean>(false);

  constructor() {
    this.isFetchingData.set(false);
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
    this.isFetchingData.set(true);
    this.albumService.getAlbums()
      .pipe(finalize(() => this.isFetchingData.set(false)))
      .subscribe(data => this.albumList.set(data));
  }

  setPendingId(id: number) {
    this.refresh();
    this.pendingId = id;
  }

  private selectAlbum(id: number) {
    this.selectedAlbum.set(this.albumList().find(album => album.id === id) ?? null);
    if (this.selectedAlbum() !== null) {
      this.isFetchingData.set(true);
      this.albumService.getPhotos(this.selectedAlbum()!.id).pipe(finalize(() => this.isFetchingData.set(false))).subscribe(photos => this.photosList.set(photos));
    }
  }

  editSelected(kwargs: Object) {
    if (this.selectedAlbum() === null) return;

    this.isFetchingData.set(true);

    const newAlbum = { ...this.selectedAlbum()!, ...kwargs }
    this.albumService.updateAlbum(this.selectedAlbum()!.id, newAlbum)
      .pipe(finalize(() => this.isFetchingData.set(false)))
      .subscribe({
        next: response => {
          console.log("PATCH " + response.status);
          this.selectedAlbum.set(newAlbum);
        },
        error: err => {
          console.log(err);
          alert("Error while changing title! Try again! " + err);
        }
      });
  }

  deleteSelected() {
    if (this.selectedAlbum() === null) return;

    this.isFetchingData.set(true);

    this.albumService.deleteAlbum(this.selectedAlbum()!.id)
      .pipe(finalize(() => this.isFetchingData.set(false)))
      .subscribe({
        next: response => {
          console.log("DELETE " + response.status);
          this.selectedAlbum.set(null);
          window.history.back();
        },
        error: err => {
          console.log(err);
          alert("Error while deleting album! Try again! " + err);
        },
      });

  }

}

