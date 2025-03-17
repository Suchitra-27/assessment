import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Group {
  id: number;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class GroupService {
  private apiUrl = 'http://127.0.0.1:8000/groups'; // Backend API URL

  constructor(private http: HttpClient) {}

  getGroups(): Observable<Group[]> {
    return this.http.get<Group[]>(this.apiUrl);
  }
}

