function [ sta ] = compute_sta( stim, rho, num_timesteps )
%COMPUTE_STA Calculates the spike-triggered average for a neuron that
%            is driven by a stimulus defined in stim. The spike-
%            triggered average is computed over num_timesteps timesteps.
    sta = zeros(num_timesteps, 1);

    % This command finds the indices of all of the spikes that occur
    % after 300 ms into the recording.
    spike_times = find(rho(num_timesteps+1:end)) + num_timesteps;
    fprintf('x is equal to %s\n',size(spike_times))
    
    % Fill in this value. Note that you should not count spikes that occur
    % before 300 ms into the recording.
    num_spikes = size(find(rho(num_timesteps+1:end) == 1), 1);
    fprintf('x is equal to %s\n',num2str(num_spikes))
    

    
    % Compute the spike-triggered average of the spikes found using the
    % find command. To do this, compute the average of all of the vectors
    % starting 300 ms (exclusive) before a spike and ending at the time of
    % the event (inclusive). Each of these vectors defines a list of
    % samples that is contained within a window of 300 ms before the each
    % spike. The average of these vectors should be completed in an
    % element-wise manner.
    % 
    % Your code goes here.
    A = zeros(num_timesteps, 1); 
    total = zeros(num_timesteps, 1);
    for i = num_timesteps+1:num_spikes
        for j = i-num_timesteps+1:i
            %fprintf("%d\n", stim(spike_times(j)));
            %fprintf('iterator: %d\n',j-(i-num_timesteps));
            A(j-(i-num_timesteps)) = stim(spike_times(j));
        end
        %fprintf("Size total: %d\n", size(total));
        %fprintf("Size A: %d\n", size(A));
        total = total + A;
    end
    
    fprintf("numSpikes: %d\n", num_spikes);
    fprintf("numTS+1: %d\n", num_timesteps+1);
    numTotal = num_spikes-(num_timesteps+1);
    fprintf("numTotal: %d\n", numTotal);
    sta = total / numTotal;
end

