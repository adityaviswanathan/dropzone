package com.dropzone.dropzone.dropscreens;

import android.hardware.Camera;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.FrameLayout;

import com.dropzone.dropzone.DropFragment;
import com.dropzone.dropzone.R;

/**
 * Created by eddie_000 on 1/17/2015.
 */
public class PhotoDrop extends Fragment implements IDropper {
    CameraPreview cameraPreview;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_photo_drop, container, false);

        // Create our Preview view and set it as the content of our activity.
        cameraPreview = new CameraPreview(getActivity(), DropFragment.camera);
        FrameLayout preview = (FrameLayout) rootView.findViewById(R.id.camera_preview);
        preview.addView(cameraPreview);

        return rootView;
    }

    public void drop() {
        // Take Picture
        DropFragment.camera.takePicture(null, null, new Camera.PictureCallback() {
            @Override
            public void onPictureTaken(byte[] data, Camera camera) {
                // TODO:
            }
        });
    }
}
