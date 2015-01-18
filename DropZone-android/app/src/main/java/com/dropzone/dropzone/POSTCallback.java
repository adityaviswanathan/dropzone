package com.dropzone.dropzone;

import org.apache.http.HttpResponse;

/**
 * Created by eddie_000 on 1/18/2015.
 */
public abstract class POSTCallback {
    public abstract void onResponse(HttpResponse response);
}
