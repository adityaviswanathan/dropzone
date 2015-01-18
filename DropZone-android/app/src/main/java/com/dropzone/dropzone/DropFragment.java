package com.dropzone.dropzone;

import android.content.Intent;
import android.hardware.Camera;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.support.v4.app.FragmentTabHost;
import android.widget.Button;
import android.widget.TabHost.TabSpec;

import com.dropzone.dropzone.dropscreens.CameraPreview;
import com.dropzone.dropzone.dropscreens.IDropper;
import com.dropzone.dropzone.dropscreens.PhotoDrop;
import com.dropzone.dropzone.dropscreens.TextDrop;
import com.dropzone.dropzone.dropscreens.VideoDrop;

/**
 * Created by eddie_000 on 1/17/2015.
 */
public class DropFragment extends Fragment {
    /**
     * The fragment argument representing the section number for this
     * fragment.
     */
    private static final String ARG_SECTION_NUMBER = "section_number";

    // Kill me
    public static Camera camera;

    public DropFragment() {
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, 1);
        setArguments(args);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_drop, container, false);
        final FragmentTabHost tabHost = (FragmentTabHost) rootView.findViewById(android.R.id.tabhost);
        tabHost.setup(getActivity(), getChildFragmentManager(), android.R.id.tabcontent);

        tabHost.addTab(tabHost.newTabSpec("text").setIndicator("Text"), TextDrop.class, null);
        tabHost.addTab(tabHost.newTabSpec("photo").setIndicator("Photo"), PhotoDrop.class, null);
        tabHost.addTab(tabHost.newTabSpec("video").setIndicator("Video"), VideoDrop.class, null);

        Button dropButton = (Button) rootView.findViewById(R.id.button_drop);
        dropButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ((IDropper) getChildFragmentManager().findFragmentByTag(tabHost.getCurrentTabTag())).drop();
            }
        });
        return rootView;
    }

    @Override
    public void onStart() {
        super.onStart();
        // Create an instance of Camera
        camera = CameraPreview.getCameraInstance();
    }

    @Override
    public void onStop() {
        camera.release();
        super.onStop();
    }
}
