import { Component, inject, OnInit, signal } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumState } from '../../services/album-state';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-album-details-component',
  imports: [FormsModule],
  templateUrl: './album-details-component.html',
  styleUrl: './album-details-component.css',
})
export class AlbumDetailsComponent implements OnInit {
  router = inject(Router);
  albumState = inject(AlbumState);
  route = inject(ActivatedRoute);


  isEditing = signal<boolean>(false);
  editFormValue = '';

  id: number = parseInt(this.route.snapshot.paramMap.get('id')!);

  ngOnInit(): void {
    this.albumState.setPendingId(this.id);
  }

  goToPhotos() {
    this.router.navigate(['/albums', this.id, 'photos']);
  }
  toggleEditAlbumName() {
    if (this.isEditing() === true) this.albumState.editSelected({ title: this.editFormValue });
    this.isEditing.set(!this.isEditing());
  }

  deleteAlbum() {
    this.albumState.deleteSelected();
  }

  goBack() {
    window.history.back();
  }

}
