import { Component, inject, OnInit, Signal, signal } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Album } from '../../models/album';
import { AlbumService } from '../../services/album-service';
import { toSignal } from '@angular/core/rxjs-interop';
import { AlbumState } from '../../services/album-state';

@Component({
  selector: 'app-album-details-component',
  imports: [],
  templateUrl: './album-details-component.html',
  styleUrl: './album-details-component.css',
})
export class AlbumDetailsComponent implements OnInit {
  router = inject(Router);
  albumState = inject(AlbumState);
  route = inject(ActivatedRoute);

  id: number = parseInt(this.route.snapshot.paramMap.get('id')!);

  ngOnInit(): void {
    this.albumState.setPendingId(this.id);
  }

  goToPhotos() {
    this.router.navigate(['/albums', this.id, 'photos']);
  }
  goBack() {
    this.router.navigate(['/albums']);
  }

}
