// En services/costume.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CostumeService {
  private apiUrl = 'http://127.0.0.1:8000/api'; 

  constructor(private http: HttpClient) {}

  getCostumes(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/costumes/`);
  }

}

